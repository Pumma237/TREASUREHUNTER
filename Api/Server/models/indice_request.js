'use strict';
module.exports = (sequelize, DataTypes) => {
  const indice_request = sequelize.define('indice_request', {
    indice_id: DataTypes.INTEGER,
    nom_indice: DataTypes.STRING,
    nom_dofusama: DataTypes.STRING,
    nom_dofusmap: DataTypes.STRING,
    resolved_by: DataTypes.INTEGER,
    resolved_when: DataTypes.DATE
  }, {});
  indice_request.associate = function(models) {
    // associations can be defined here
  };
  return indice_request;
};