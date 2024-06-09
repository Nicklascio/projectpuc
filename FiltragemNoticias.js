document.addEventListener('DOMContentLoaded', function() {
    // Elementos do DOM
    const levelSelect = document.getElementById('investor-level');
    const newsContainer = document.getElementById('news-container');

    // Evento de mudança no nível do investidor
    levelSelect.addEventListener('change', function() {
        const level = levelSelect.value;
        fetchNews(level);
    });

    // Função para buscar notícias da API
    function fetchNews(level) {
        fetch(`/api/news?level=${level}`)
            .then(response => response.json())
            .then(data => {
                displayNews(data);
            })
            .catch(error => {
                console.error('Erro ao buscar notícias:', error);
            });
    }

    // Função para exibir as notícias na página
    function displayNews(articles) {
        newsContainer.innerHTML = '';
        articles.forEach(article => {
            const articleDiv = document.createElement('div');
            articleDiv.className = 'news-article';
            articleDiv.innerHTML = `
                <h2>${article.title}</h2>
                <p>${article.content}</p>
                <a href="${article.url}" target="_blank">Read more</a>
            `;
            newsContainer.appendChild(articleDiv);
        });
    }

    // Buscar notícias iniciais para nível iniciante
    fetchNews('beginner');
});