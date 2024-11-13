from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `posts` ALTER COLUMN `content` DROP DEFAULT;
        ALTER TABLE `posts` MODIFY COLUMN `content` JSON;
        ALTER TABLE `posts` ALTER COLUMN `title` SET DEFAULT '未命名';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `posts` MODIFY COLUMN `content` JSON NOT NULL;
        ALTER TABLE `posts` ALTER COLUMN `content` SET;
        ALTER TABLE `posts` ALTER COLUMN `title` DROP DEFAULT;"""
