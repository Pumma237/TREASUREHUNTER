'use strict';
module.exports = (sequelize, DataTypes) => {
  const personnage_zaap = sequelize.define('personnage_zaap', {
    id_personnage: DataTypes.INTEGER,
    id_zaap: DataTypes.INTEGER
  }, {});
  personnage_zaap.associate = function(models) {
    // associations can be defined here
  };
  return personnage_zaap;
};