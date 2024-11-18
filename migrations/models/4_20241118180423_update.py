from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
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
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `todoitem`;"""
