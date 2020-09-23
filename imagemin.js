const imagemin = require("imagemin-keep-folder");
const imageminPngquant = require("imagemin-pngquant");
const imageminMozjpeg = require("imagemin-mozjpeg");

imagemin(['output/**/*.{jpg,png}'], {
  use: [
    imageminMozjpeg({
      quality: 60,
    }),
    imageminPngquant({
      quality: [0.7, 0.8],
    }),
  ],
}).then(files => { 
  console.log(files);
});
