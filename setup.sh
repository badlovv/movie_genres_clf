mkdir -p ~/.streamlit/
echo "[general]
email = \"vvbadlo@edu.hse.ru\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml