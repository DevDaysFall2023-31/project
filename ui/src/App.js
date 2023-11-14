import React from 'react';
import './styles/App.css';
import { Header } from './components/Header';
import { BlockMain } from './components/BlockMain';
import { BlockMusic } from './components/BlockMusic';

function App() {
  return (
    <div className="App">
      <Header />
      <BlockMain />
      <BlockMusic
        albumInfo={
          {
            img: "https://avatars.yandex.net/get-music-content/149669/01b939f1.a.8472613-1/m1000x1000?webp=false",
            title: "Subtitle playlist name",
            description: "Учитывая ключевые сценарии поведения, разбавленное изрядной долей эмпатии, рациональное мышление создаёт необходимость включения в производственный план целого ряда внеочередных мероприятий с учётом комплекса поставленных обществом задач.",
            ymusic: "#"
          }
        }
      />
    </div>
  );
}

export default App;
