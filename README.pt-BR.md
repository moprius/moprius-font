# Família tipográfica Moprius

[Read in English](README.md)

Moprius é um sistema tipográfico aberto formado por três famílias coordenadas para interfaces, programação e leitura prolongada.

- **Moprius Sans 1.437** — sem serifa proporcional para interfaces e textos de uso geral.
- **Moprius Mono 1.437** — monoespaçada para terminais, editores e código-fonte.
- **Moprius Serif 1.000** — serifada para livros, artigos, ensaios e textos longos.

A coleção contém **12 fontes estáticas**: Regular, Italic, Bold e Bold Italic em cada família.

![Moprius Sans e Mono](specimen/Moprius-Sans-Mono-Specimen.png)

![Moprius Serif](specimen/Moprius-Serif-Specimen.png)

## Arquivos incluídos

| Família | Formato para desktop | Formato web | Estilos |
|---|---|---|---|
| Moprius Sans | TTF | WOFF2 | Regular, Italic, Bold, Bold Italic |
| Moprius Mono | TTF | WOFF2 | Regular, Italic, Bold, Bold Italic |
| Moprius Serif | OTF | WOFF2 | Regular, Italic, Bold, Bold Italic |

## Instalação no Linux

```bash
./install-linux.sh
```

Instalação manual:

```bash
mkdir -p ~/.local/share/fonts/Moprius
cp fonts/ttf/*.ttf fonts/otf/*.otf ~/.local/share/fonts/Moprius/
fc-cache -f
```

Para remover:

```bash
./uninstall-linux.sh
```

## Uso na web

Importe `css/moprius.css`:

```css
body { font-family: "Moprius Serif", serif; }
.interface { font-family: "Moprius Sans", sans-serif; }
code { font-family: "Moprius Mono", monospace; }
```

A demonstração em `docs/index.html` pode ser publicada diretamente pelo GitHub Pages.

## Estrutura do repositório

```text
fonts/ttf/       Moprius Sans e Mono para desktop
fonts/otf/       Moprius Serif para desktop
fonts/woff2/     Fontes web das três famílias
sources/ttx/     Fontes editáveis em OpenType XML
tools/           Ferramentas de compilação e auditoria
css/             Folha @font-face combinada
docs/            Demonstração para GitHub Pages
specimen/        Amostras visuais
audits/          Relatórios das auditorias
```

## Compilação e auditoria

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python tools/build.py
python tools/audit.py
```

O GitHub Actions executa a auditoria automaticamente a cada envio e pull request.

## Nomes e origem

Versões antigas de desenvolvimento da Sans e da Mono usavam “Moprius Source”. Os nomes públicos corretos são **Moprius Sans**, **Moprius Mono** e **Moprius Serif**. A palavra **Source** é um nome reservado nas licenças originais da Adobe e aparece apenas nos créditos históricos.

A coleção reúne versões modificadas de trabalhos licenciados pela OFL, incluindo Adobe Source Sans, Adobe Source Serif e Fantasque Sans Mono. Os autores originais não endossam este projeto.

## Licença

As fontes, arquivos editáveis e ferramentas de compilação são distribuídos sob a **SIL Open Font License 1.1**. Consulte `OFL.txt`, `LICENSE.txt` e `LEGAL-NOTICES.md`.

Versão da coleção: **v1.0.0**  
Versão da Sans/Mono: **1.437**  
Versão da Serif: **1.000**
