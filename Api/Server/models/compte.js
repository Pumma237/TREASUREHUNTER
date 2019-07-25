'use strict';
module.exports = (sequelize, DataTypes) => {
  const compte = sequelize.define('compte', {
    pseudo: DataTypes.STRING,
    email: DataTypes.STRING,
    password: DataTypes.STRING,
    token: DataTypes.STRING,
    abonnement: DataTypes.DATE
  }, {});
  compte.associate = function(models) {
    // associations can be defined here
  };
  return compte;
};