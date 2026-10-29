# Radostina Dacheva — portfolio за GitHub Pages

Това е копие на готовото портфолио, с всички снимки, видеа, шрифтове и контактната форма.

## Публикуване

1. Създай GitHub профил или влез в съществуващия.
2. Създай **public** repository с име `USERNAME.github.io`, като замениш USERNAME с действителното си потребителско име. Например само ако профилът ти е `radostinadacheva`, името е `radostinadacheva.github.io`.
3. Разархивирай пакета и качи съдържанието на папката `github-pages-portfolio` в главната директория на repository-то. Запази папките `dist`, `scripts` и `.github`. Не качвай самия ZIP. За много файлове най-удобно е GitHub Desktop; през браузър GitHub приема до 100 файла наведнъж.
4. В repository → **Settings → Pages → Build and deployment → Source**, избери **GitHub Actions**.
5. В **Actions → Publish portfolio → Run workflow** стартирай публикуването за `main` (или изчакай автоматичното изпълнение при качване).
6. При успешно изпълнение сайтът е на `https://USERNAME.github.io/`. Възможно е да отнеме няколко минути.

Адресите за търсачки и sitemap се актуализират автоматично към действителния GitHub профил при публикуване. Не е необходима покупка на домейн. Сегашният сайт не се променя от този пакет.

## Следващи промени

Съдържанието на сайта е в `dist`. При промяна и публикуване на нов commit в `main` сайтът се обновява автоматично. Контактната форма използва същия Formspree адрес. Ако си включила ограничения по домейн в Formspree, разреши и новия адрес.

Официални инструкции:
- https://docs.github.com/en/pages/quickstart
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
