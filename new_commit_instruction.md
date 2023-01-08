# Robienie nowego feature:

## Po stronie terminala

1) nowy branch: `git checkout -b nazwa-brancha`
2) pisanie kodu
3) sprawdzenie w jakich plikach dokonano zmian: `git status`
4) dodanie interesujących Cie plików do commita
5) napisanie wiadomości commita: `git commit -m "komunikat"` lub `git commit` i napisanie wiadomości w oknie
6) wysłanie commita na brancha:
  - gdy jeszcze nie istnieje na githubie: `git push -u origin nazwa-brancha`
  - gdy już istnieje (któryś z rzędu commit na branchu): `git push`
7) Możesz tak wysłać kilka commitów

## Teraz przechodzimy do githuba w  przeglądarce

8) utworzenie pull reguesta (merge requesta), poproszenie kogoś o review
9) merge na mastera zielonym przyciskiem w zakładce **conversation**

## Po stronie terminala
10) przechodzimy na brancha **main** lub **master**: `git checkout main`
11) fetchowanie zmian: `git fetch`
12) pobranie zmian: `git pull`
