'use strict';
module.exports = (sequelize, DataTypes) => {
  const zaap = sequelize.define('zaap', {
    id_map: DataTypes.INTEGER,
    y: DataTypes.INTEGER,
    x: DataTypes.INTEGER,
    nom: DataTypes.STRING
  }, {});
  zaap.associate = function(models) {
    // associations can be defined here
  };
  return zaap;
};