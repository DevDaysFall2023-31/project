import React, { useState } from 'react';
import './styles/App.css';
import { Header } from './components/Header';
import { BlockMain } from './components/BlockMain';
import { BlockMusic } from './components/BlockMusic';

function App() {
  const [blocksMusic, setBlocksMusic] = useState([]);
  const createMusicBlock = (newBlockMusic: never) => {
    setBlocksMusic([...blocksMusic, newBlockMusic]);
  }
  return (
    <div className="App">
      <Header />
      <BlockMain create={ createMusicBlock }  />
      {
        blocksMusic.map(blockMusic => {
          return <BlockMusic
                    albumInfo={blockMusic}
                    create={createMusicBlock}
                    // key={blockMusic.id}
                />
        })
      }
    </div>
  );
}

export default App;