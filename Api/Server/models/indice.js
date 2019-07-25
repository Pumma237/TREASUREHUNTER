'use strict';
module.exports = (sequelize, DataTypes) => {
  const indice = sequelize.define('indice', {
    id_dofus: DataTypes.INTEGER,
    nom_dofus: DataTypes.STRING,
    nomdofusama: DataTypes.STRING,
    nom_dofusmap: DataTypes.STRING
  }, {});
  indice.associate = function(models) {
    // associations can be defined here
  };
  return indice;
};