// postcss.config.js
const path = require("path")
const POSTCSSCHAIN = process.env.POSTCSSCHAIN === 'production';

const purgecss = require('@fullhuman/postcss-purgecss')({

  content: [
    path.resolve(__dirname, "./themes/milena/templates/*.html")
  ],

  // extract class names from templates
  defaultExtractor: content => {
    const broadMatches = content.match(/[^<>"'`\s]*[^<>"'`\s:]/g) || []
    const innerMatches = content.match(/[^<>"'`\s.()]*[^<>"'`\s.():]/g) || []
    return broadMatches.concat(innerMatches)
  }
})

module.exports = {
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
    POSTCSSCHAIN ? purgecss : "",
  ]
}
