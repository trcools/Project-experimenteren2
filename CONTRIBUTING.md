# Bijdragen aan Project Experimenteren 2

Bedankt voor je interesse om bij te dragen aan dit project! Dit document bevat richtlijnen voor effectieve samenwerking.

## 🎯 Hoe te Beginnen

### 1. Repository Setup
- Fork het repository (optioneel voor team members)
- Clone je fork lokaal
- Voeg de originele repository toe als upstream:
  ```bash
  git remote add upstream https://github.com/trcools/Project-experimenteren2.git
  ```

### 2. Branch Strategie
- `main` - Stabiele productie code
- `develop` - Development branch voor integratie
- `feature/*` - Nieuwe features
- `bugfix/*` - Bug fixes
- `hotfix/*` - Urgente fixes voor productie

### 3. Workflow voor Nieuwe Features
1. **Sync je lokale repository**:
   ```bash
   git checkout main
   git pull origin main
   ```

2. **Maak een nieuwe branch**:
   ```bash
   git checkout -b feature/beschrijvende-naam
   ```

3. **Maak je wijzigingen**:
   - Schrijf duidelijke, beschrijvende code
   - Voeg commentaar toe waar nodig
   - Test je wijzigingen grondig

4. **Commit je wijzigingen**:
   ```bash
   git add .
   git commit -m "feat: beschrijving van je feature"
   ```

5. **Push naar GitHub**:
   ```bash
   git push origin feature/beschrijvende-naam
   ```

6. **Open een Pull Request**:
   - Geef een duidelijke titel en beschrijving
   - Link naar gerelateerde issues
   - Wacht op code review van teamleden

## 📝 Commit Message Richtlijnen

Gebruik duidelijke commit messages met het volgende formaat:
```
<type>: <korte beschrijving>

[optionele uitgebreide beschrijving]

[optionele footer]
```

### Types:
- `feat`: Nieuwe feature
- `fix`: Bug fix
- `docs`: Documentatie wijzigingen
- `style`: Code formatting (geen functionaliteit wijziging)
- `refactor`: Code refactoring
- `test`: Test toevoegingen of wijzigingen
- `chore`: Onderhoud taken

### Voorbeelden:
```
feat: voeg gebruiker authenticatie toe
fix: los crash op bij het opslaan van data
docs: update README met installatie instructies
```

## 👀 Code Review Process

### Voor de Reviewer:
- Controleer of de code functioneel correct is
- Let op code kwaliteit en leesbaarheid
- Test de wijzigingen lokaal indien nodig
- Geef constructieve feedback
- Approve de PR als alles in orde is

### Voor de Author:
- Reageer op feedback
- Maak gevraagde wijzigingen
- Update de PR
- Merge pas na approval van minimaal één teamlid

## 🐛 Bug Reports

Bij het rapporteren van een bug, vermeld:
- Beschrijving van het probleem
- Stappen om te reproduceren
- Verwacht gedrag
- Actueel gedrag
- Screenshots indien relevant
- Environment details (OS, browser, etc.)

## 💡 Feature Requests

Bij het voorstellen van een feature:
- Duidelijke beschrijving van de feature
- Use case / probleem dat het oplost
- Mogelijke implementatie suggesties
- Alternatieven die je hebt overwogen

## 🤝 Communicatie

- Gebruik duidelijke en respectvolle taal
- Stel vragen als iets onduidelijk is
- Deel kennis en help elkaar
- Wees open voor feedback

## ✅ Checklist voor Pull Requests

- [ ] Code volgt de project stijl
- [ ] Wijzigingen zijn getest
- [ ] Documentatie is bijgewerkt
- [ ] Commit messages zijn duidelijk
- [ ] Branch is up-to-date met main
- [ ] Geen merge conflicts
- [ ] Code review is aangevraagd

## 📚 Aanvullende Resources

- [Git Basics](https://git-scm.com/book/en/v2)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)

Bedankt voor je bijdrage! 🎉
