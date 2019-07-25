'use strict';
module.exports = (sequelize, DataTypes) => {
  const indice_find = sequelize.define('indice_find', {
    nmb_screen: DataTypes.INTEGER,
    resolved_by: DataTypes.INTEGER,
    resolved_when: DataTypes.DATE
  }, {});
  indice_find.associate = function(models) {
    // associations can be defined here
  };
  return indice_find;
};