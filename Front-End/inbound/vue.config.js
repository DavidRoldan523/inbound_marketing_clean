module.exports = {
    //...
    devServer: {
      proxy:  'http://104.131.169.113:8003',
      open: process.platform === 'darwin',
      host: '0.0.0.0',
      port: 8004, //CHANGE YOUR PORT HERE!
      https: false,
      hotOnly: false,
    },
    //...
  }