-- CreateTable
CREATE TABLE `partidos_politicos` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(45) NOT NULL,
    `logo` TEXT NOT NULL,

    UNIQUE INDEX `partidos_politicos_nombre_key`(`nombre`),
    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `regiones` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(45) NOT NULL,

    UNIQUE INDEX `regiones_nombre_key`(`nombre`),
    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `votantes` (
    `dni` VARCHAR(8) NOT NULL,
    `nombre` TEXT NOT NULL,
    `apellido` TEXT NOT NULL,
    `region` TEXT NOT NULL,

    PRIMARY KEY (`dni`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `candidatos` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `nombre` TEXT NOT NULL,
    `apellido` TEXT NOT NULL,
    `partido_politico_id` INTEGER NOT NULL,
    `region_id` INTEGER NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `sufragios` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `fecha` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `votante_id` VARCHAR(8) NOT NULL,
    `candidato_id` INTEGER NOT NULL,

    UNIQUE INDEX `sufragios_votante_id_key`(`votante_id`),
    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `candidatos` ADD CONSTRAINT `candidatos_partido_politico_id_fkey` FOREIGN KEY (`partido_politico_id`) REFERENCES `partidos_politicos`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `candidatos` ADD CONSTRAINT `candidatos_region_id_fkey` FOREIGN KEY (`region_id`) REFERENCES `regiones`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `sufragios` ADD CONSTRAINT `sufragios_votante_id_fkey` FOREIGN KEY (`votante_id`) REFERENCES `votantes`(`dni`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `sufragios` ADD CONSTRAINT `sufragios_candidato_id_fkey` FOREIGN KEY (`candidato_id`) REFERENCES `candidatos`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;
