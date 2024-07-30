const dgram = require('unix-dgram'); // UNIXドメインソケット用のライブラリ
const path = '/tmp/socket_file'; // サーバーと同じパスに設定
const client = dgram.createSocket('unix_dgram');

// サーバーにメッセージを送信する
const request = JSON.stringify({
  method: 'floor',
  params: [35.546],
  param_types: ['number'],
  id: 1
});


client.on('message', (msg) => {
  try {
    const response = JSON.parse(msg.toString());
    console.log('Server response:', response);
  } catch (err) {
    console.error('Error parsing response:', err);
  } finally {
    client.close();
  }
});


client.send(Buffer.from(request), 0, request.length, path, (err) => {
  if (err) {
    console.error('Error sending request:', err);
    client.close();
  } else {
    console.log('Request sent');
  }
});