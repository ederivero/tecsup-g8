/*
  Warnings:

  - Made the column `regionId` on table `votantes` required. This step will fail if there are existing NULL values in that column.

*/
-- DropForeignKey
ALTER TABLE `votantes` DROP FOREIGN KEY `votantes_regionId_fkey`;

-- AlterTable
ALTER TABLE `votantes` MODIFY `regionId` INTEGER NOT NULL;

-- AddForeignKey
ALTER TABLE `votantes` ADD CONSTRAINT `votantes_regionId_fkey` FOREIGN KEY (`regionId`) REFERENCES `regiones`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;
