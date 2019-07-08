module.exports = {
    //...
    devServer: {
      open: process.platform === 'darwn',
      host: '0.0.0.0',
      port: 8004, //CHANGE YOUR PORT HERE!
      https: false,
      hotOnly: false,
    },
    //...
  }