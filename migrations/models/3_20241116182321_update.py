from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `user` ADD `avatar_url` VARCHAR(255);
        ALTER TABLE `user` MODIFY COLUMN `salt` LONGBLOB;
        ALTER TABLE `user` MODIFY COLUMN `password_hash` LONGBLOB;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `user` DROP COLUMN `avatar_url`;
        ALTER TABLE `user` MODIFY COLUMN `salt` LONGBLOB NOT NULL;
        ALTER TABLE `user` MODIFY COLUMN `password_hash` LONGBLOB NOT NULL;"""
