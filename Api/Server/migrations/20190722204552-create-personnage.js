'use strict';
module.exports = {
  up: (queryInterface, Sequelize) => {
    return queryInterface.createTable('personnages', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      id_compte: {
        type: Sequelize.INTEGER
      },
      pseudo: {
        type: Sequelize.STRING
      },
      token: {
        type: Sequelize.STRING
      },
      lvl_perso: {
        type: Sequelize.INTEGER
      },
      lvl_chasse: {
        type: Sequelize.INTEGER
      },
      nmb_chasse: {
        type: Sequelize.INTEGER
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE
      }
    });
  },
  down: (queryInterface, Sequelize) => {
    return queryInterface.dropTable('personnages');
  }
};