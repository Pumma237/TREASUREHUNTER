'use strict';
module.exports = {
  up: (queryInterface, Sequelize) => {
    return queryInterface.createTable('indice_requests', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      id_indice: {
        type: Sequelize.INTEGER
      },
      nom_indice: {
        type: Sequelize.STRING
      },
      nom_dofusama: {
        type: Sequelize.STRING
      },
      nom_dofusmap: {
        type: Sequelize.STRING
      },
      resolved_by: {
        type: Sequelize.INTEGER
      },
      resolved_when: {
        type: Sequelize.DATE
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
    return queryInterface.dropTable('indice_requests');
  }
};