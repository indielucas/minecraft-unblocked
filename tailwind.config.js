module.exports = {
    content: [
        "./theme/templates/**/*.html",
    ],
    daisyui: {
        themes: [
            "light",
            "dark",
            "synthwave"
        ]
    },
    theme: {
        extend: {},
    },
    plugins: [require("@tailwindcss/typography"), require("daisyui")],
}