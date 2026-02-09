# Quick Start Gids - Project Experimenteren 2

Welkom bij het team! Deze gids helpt je om snel aan de slag te gaan.

## 1. Account Setup

### GitHub Account
- Zorg dat je een GitHub account hebt
- Vraag toegang tot de repository aan
- Stel twee-factor authenticatie in (aanbevolen)

### Git Configuratie
```bash
# Configureer je naam en email
git config --global user.name "Jouw Naam"
git config --global user.email "jouw.email@example.com"

# Optioneel: configureer je standaard editor
git config --global core.editor "code --wait"  # Voor VS Code
```

## 2. Repository Clonen

```bash
# Clone het repository
git clone https://github.com/trcools/Project-experimenteren2.git

# Navigeer naar de project directory
cd Project-experimenteren2
```

## 3. Belangrijke Documenten Lezen

Lees de volgende documenten om bekend te raken met het project:
1. [README.md](../README.md) - Project overzicht
2. [CONTRIBUTING.md](../CONTRIBUTING.md) - Samenwerking richtlijnen
3. [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md) - Gedragscode
4. [docs/project-overview.md](./project-overview.md) - Gedetailleerd project overzicht

## 4. Development Environment Setup

[Voeg specifieke setup instructies toe voor jullie project, bijvoorbeeld:]

```bash
# Installeer dependencies (bijvoorbeeld voor Node.js)
# npm install

# Voor Python projecten
# pip install -r requirements.txt

# Voor Java projecten
# mvn install
```

## 5. Je Eerste Taak

### Stap 1: Pak een Issue
- Ga naar de [Issues](https://github.com/trcools/Project-experimenteren2/issues) pagina
- Zoek een issue gelabeld met `good first issue` of `help wanted`
- Assign het issue aan jezelf of laat een comment achter

### Stap 2: Maak een Branch
```bash
# Zorg dat je main branch up-to-date is
git checkout main
git pull origin main

# Maak een nieuwe branch
git checkout -b feature/jouw-feature-naam
```

### Stap 3: Maak Wijzigingen
- Werk aan je feature of fix
- Test je wijzigingen lokaal
- Commit regelmatig met duidelijke messages

```bash
# Stage je wijzigingen
git add .

# Commit met een duidelijke message
git commit -m "feat: beschrijving van je wijziging"
```

### Stap 4: Push en Open een PR
```bash
# Push je branch naar GitHub
git push origin feature/jouw-feature-naam
```

- Ga naar GitHub en open een Pull Request
- Vul het PR template in
- Vraag om code review

## 6. Dagelijkse Workflow

### Sync met Main
```bash
# Haal de laatste wijzigingen op
git checkout main
git pull origin main

# Update je feature branch
git checkout feature/jouw-feature
git merge main
```

### Voor je aan Nieuwe Wijzigingen Begint
1. Pull de laatste wijzigingen van main
2. Maak een nieuwe branch
3. Werk aan je taak
4. Test grondig
5. Push en open een PR

## 7. Hulp Nodig?

### Waar vind je Hulp?
- **Documentatie**: Check de `docs/` folder
- **Issues**: Zoek in bestaande issues
- **Teamleden**: Tag een teamlid in een comment
- **GitHub Discussions**: Voor algemene vragen

### Nuttige Git Commando's
```bash
# Check status van je repository
git status

# Zie de geschiedenis
git log --oneline

# Zie wijzigingen die nog niet gecommit zijn
git diff

# Annuleer wijzigingen aan een file
git checkout -- <filename>

# Switch tussen branches
git checkout <branch-name>

# List alle branches
git branch -a
```

## 8. Best Practices

### Do's ✅
- Commit regelmatig met duidelijke messages
- Pull wijzigingen van main voordat je begint
- Test je code voor je pusht
- Vraag om hulp als je vast zit
- Review code van anderen
- Houd documentatie up-to-date

### Don'ts ❌
- Commit niet direct naar main
- Push geen credentials of gevoelige data
- Maak geen te grote commits
- Vergeet niet te testen
- Werk niet aan taken die al toegewezen zijn

## 9. Checklist voor Nieuwe Teamleden

- [ ] GitHub account aangemaakt
- [ ] Toegang tot repository verkregen
- [ ] Git geconfigureerd op lokale machine
- [ ] Repository gecloned
- [ ] Belangrijke documenten gelezen
- [ ] Development environment opgezet
- [ ] Eerste branch aangemaakt
- [ ] Eerste commit gemaakt
- [ ] Contact opgenomen met het team

## 10. Volgende Stappen

Nu je alles hebt ingesteld:
1. Maak jezelf bekend aan het team
2. Vraag om een taak of pak een `good first issue`
3. Stel vragen als je die hebt
4. Begin met coderen! 🚀

---

Welkom bij het team! We kijken ernaar uit om met je samen te werken. 🎉
