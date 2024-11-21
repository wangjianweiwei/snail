from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `user` ADD `avatar_url` VARCHAR(255);
        ALTER TABLE `user` ADD `otp_code` VARCHAR(32) NOT NULL UNIQUE;
        ALTER TABLE `user` MODIFY COLUMN `salt` LONGBLOB;
        ALTER TABLE `user` MODIFY COLUMN `password_hash` LONGBLOB;
        CREATE TABLE IF NOT EXISTS `todoitem` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `title` VARCHAR(255) NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_completed` BOOL NOT NULL  DEFAULT 0,
    `completed_at` DATETIME(6),
    `plan_at` DATE,
    `priority` SMALLINT NOT NULL  DEFAULT 100,
    KEY `idx_todoitem_plan_at_126f95` (`plan_at`),
    KEY `idx_todoitem_priorit_42122d` (`priority`)
) CHARACTER SET utf8mb4;
        ALTER TABLE `user` ADD UNIQUE INDEX `uid_user_otp_cod_b2248b` (`otp_code`);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `user` DROP INDEX `idx_user_otp_cod_b2248b`;
        ALTER TABLE `user` DROP COLUMN `avatar_url`;
        ALTER TABLE `user` DROP COLUMN `otp_code`;
        ALTER TABLE `user` MODIFY COLUMN `salt` LONGBLOB NOT NULL;
        ALTER TABLE `user` MODIFY COLUMN `password_hash` LONGBLOB NOT NULL;
        DROP TABLE IF EXISTS `todoitem`;"""
