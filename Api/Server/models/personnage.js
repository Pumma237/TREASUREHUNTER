'use strict';
module.exports = (sequelize, DataTypes) => {
  const personnage = sequelize.define('personnage', {
    id_compte: DataTypes.INTEGER,
    pseudo: DataTypes.STRING,
    token: DataTypes.STRING,
    lvl_perso: DataTypes.INTEGER,
    lvl_chasse: DataTypes.INTEGER,
    nmb_chasse: DataTypes.INTEGER
  }, {});
  personnage.associate = function(models) {
    // associations can be defined here
  };
  return personnage;
};