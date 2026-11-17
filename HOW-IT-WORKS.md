# How News Tiles works

```
  Live TV & radio from around the world          News & conflict reports
                 │                                          │
                 ▼                                          ▼
        ┌─────────────────┐                     ┌────────────────────┐
        │   Tiles wall    │                     │  War Room / News   │
        │ 1·4·9·16 screens│                     │  Room data service │
        └────────┬────────┘                     └─────────┬──────────┘
                 │ the sound you choose                   │ places, types, times
                 ▼                                        ▼
        ┌─────────────────┐                     ┌────────────────────┐
        │ Live translation│                     │  Live map + alerts │
        │ voice & captions│                     │  (strikes, ground,  │
        │ in your language│                     │  aircraft)        │
        └─────────────────┘                     └────────────────────┘
                 │                                        │
                 └──────────────► You ◄───────────────────┘
          website · browser extension · Android TV app — in 28 languages
```

## The pieces

| Part | What it does |
| --- | --- |
| Website | The tiles wall, War Room and News Room, served worldwide from the edge. |
| Live translation | Listens to the broadcast you pick and speaks and captions it in your language in real time. |
| War Room | Gathers conflict reports, places them on a map, sorts them by type, and alerts you once per event. |
| News Room | Reads local news sources for a country, places each story on the map and translates it. |
| Languages | One master list of every on-screen phrase, translated into 28 languages and checked before each release. |
| Android TV app & extension | The same experience on a TV and in the browser. |

## How it's built and shipped

- One person directs AI coding agents; written rules tell every agent what must never change.
- Every change goes to a private test site first, is checked, and goes live only with the owner's approval.
- Each release is numbered and recorded, so any change can be traced or rolled back.
