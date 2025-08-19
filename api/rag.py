import asyncio
import ssl
from asyncio import Queue

from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import StreamingResponse

ssl._create_default_https_context = ssl._create_unverified_context
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch

router = APIRouter()

queues = {}

llm = init_chat_model("deepseek-chat", model_provider="deepseek")
embedding_model = DashScopeEmbeddings(model="text-embedding-v1")

loader = DirectoryLoader("./data", glob="*.txt")
documents = loader.load()
vector_store = DocArrayInMemorySearch.from_documents(documents, embedding_model)

template = ChatPromptTemplate.from_messages([("user", """你是美团客服机器人，你的任务是根据下述给定的已知信息回答用户的问题
    已知信息：{context}
    用户问题：{question}
    如果已知信息中不包含用户问题的答案，或者已知信息不足以回答用户的问题，可以自由发挥，但是你要告诉用户仅供参考”。
    请用中文回答用户的问题""")])


async def answer(q, queue: Queue):
    retriever = vector_store.as_retriever()
    segments = await retriever.ainvoke(q, k=2)

    context = []
    for segment in segments:
        context.append(segment.page_content)

    prompt = template.invoke({"context": context, "question": q})
    async for n in llm.astream(prompt):
        await queue.put(n.content)


# 生成 SSE 数据的生成器
async def event_generator(queue: Queue):
    while True:
        try:
            message = await queue.get()
        except asyncio.CancelledError:
            break
        # SSE 协议要求每条消息以 "data:" 开头，并以 "\n\n" 结束
        yield f"data:{message}\n\n"
    # 结束时可以发送一个特殊消息
    yield "data:\n\n"


@router.get("/sse")
async def sse(talk_id: str):
    """
    TODO: 根据会话ID创建消息队列，进行消息推送
    :return:
    """
    print(talk_id)
    queues[talk_id] = queue = Queue()
    return StreamingResponse(event_generator(queue), media_type="text/event-stream")


@router.get("/q")
async def question(talk_id: str, q: str, background_tasks: BackgroundTasks):
    queue = queues[talk_id]
    background_tasks.add_task(answer, q, queue)

    return {"status": "ok"}
