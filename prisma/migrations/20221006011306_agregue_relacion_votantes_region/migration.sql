/*
  Warnings:

  - You are about to drop the column `region` on the `votantes` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE `votantes` DROP COLUMN `region`,
    ADD COLUMN `regionId` INTEGER NULL;

-- AddForeignKey
ALTER TABLE `votantes` ADD CONSTRAINT `votantes_regionId_fkey` FOREIGN KEY (`regionId`) REFERENCES `regiones`(`id`) ON DELETE SET NULL ON UPDATE CASCADE;
