const TelegramBot = require('node-telegram-bot-api');

// Token bot Telegram Anda
const token = '7511141394:AAGlQDpJ2WQ2WqBSbHthWmEchVzJzxL1_1k';

// Daftar method
const methodList = ['List 1', 'List 2'];

// Inisialisasi bot
const bot = new TelegramBot(token, { polling: true });

// Mendengarkan command /start
bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, 'Halo! Saya bot Anda. Gunakan /ca untuk melihat cara penggunaan dan daftar method atau /ci host port time method untuk menjalankan perintah tertentu.');
});

// Mendengarkan command /ca
bot.onText(/\/ca/, (msg) => {
  const chatId = msg.chat.id;

  // Menampilkan cara penggunaan dan daftar metode
  bot.sendMessage(chatId, 'Cara penggunaan: /ci host port time method\nContoh: /ci https://file.cunhua.today 433 60 TLS');
  bot.sendMessage(chatId, 'Daftar Metode:');
  methodList.forEach((method) => bot.sendMessage(chatId, `- ${method}`));
});

// Mendengarkan command /ci host port time method
bot.onText(/\/ci (.+)/, (msg, match) => {
  const chatId = msg.chat.id;
  const command = match[1].split(' ');

  if (command.length === 4) {
    const [host, port, time, method] = command;
    const apiUrl = `http://url atau ip kalo ip ip lu:port lu/api?key=kontollodon&host=${host}&port=${port}&time=${time}&method=${method}`;

    // Mengirimkan pesan berhasil ke pengguna Telegram tanpa menambahkan "API URL"
    bot.sendMessage(chatId, `Berhasil Pada ${host} ${port} ${time} ${method}`);
    // Jika Anda masih ingin menyimpan apiUrl untuk penggunaan di tempat lain
    // console.log(apiUrl);
  } else {
    // Menangani format perintah yang salah
    bot.sendMessage(chatId, 'Format perintah salah. Pastikan formatnya seperti ini:\n/ci host port time method');
    bot.sendMessage(chatId, 'Contoh: /ci https://file.cunhua.today 433 60 TLS');
    bot.sendMessage(chatId, 'Ketika salah penulisan, pastikan tidak ada spasi ekstra dan urutannya benar.');
  }
});
