const imagemin = require("imagemin-keep-folder");
const imageminPngquant = require("imagemin-pngquant");
const imageminMozjpeg = require("imagemin-mozjpeg");

(async () => {
  await imagemin(["output/**/*.{jpg,png}"], {})
    .catch(() => {
      console.error;
      console.log("There were problems with post-processing the images.")
      process.exit(1);
    })
    .then((files) => {
      console.log(files);
      use: [
        imageminMozjpeg({
          quality: [0.7, 0.8],
        }),
        imageminPngquant({
          quality: [0.7, 0.8],
        }),
      ];
    });
  console.log("All images were successfully resized");
})();
