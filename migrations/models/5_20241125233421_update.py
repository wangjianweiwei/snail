from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `user` DROP COLUMN `password_hash`;
        ALTER TABLE `user` DROP COLUMN `salt`;
        ALTER TABLE `posts` ADD `wordcount` INT NOT NULL  DEFAULT 0;
        DROP TABLE IF EXISTS `third_party_auth`;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `user` ADD `password_hash` LONGBLOB;
        ALTER TABLE `user` ADD `salt` LONGBLOB;
        ALTER TABLE `posts` DROP COLUMN `wordcount`;"""
