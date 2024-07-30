import net from 'net';

const path = '/tmp/socket_file'; // サーバーと同じパスに設定

const client = net.createConnection(path);

client.on('connect', () => {
  console.log('connected.');

  // 送信するメッセージを JSON 文字列に変換
  const message = JSON.stringify({
    method: 'floor',
    params: [35.546],
    param_types: ['number'],
    id: 1
  });

  // メッセージをサーバーに送信
  client.write(message);
});

client.on('data', (data) => {
  console.log('Server response:', data.toString());
  client.end(); // サーバーからのレスポンスを受け取った後に接続を終了
});

client.on('end', () => {
  console.log('disconnected.');
});

client.on('error', (err) => {
  console.error('Error:', err.message);
  client.end(); // エラー発生時に接続を終了
});
