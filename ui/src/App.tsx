import React, { useEffect, useState } from 'react';
import './styles/App.css';
import { Header } from './components/Header';
import { BlockMain } from './components/BlockMain';
import { BlockMusic } from './components/BlockMusic';
import { YaTokenForm } from './components/YaToken';
import supabase from './supabase';
import { GetTrackSchema, GetTracksListSchema } from './generated';
import api from './api';

function App() {
  const [blocksMusic, setBlocksMusic] = useState<GetTrackSchema[]>([]);
  const createMusicBlock = (newBlockMusic: any, index: any) => {
    const blocks = blocksMusic.slice(0, index);
    setBlocksMusic([...blocks, newBlockMusic]);
  }

  const [ya_token, setYaToken] = useState<boolean>(false);

  useEffect(() => {
    async function getYaToken() {
      const user = await supabase.auth.getUser();
      if ('ya_token' in user.data.user.user_metadata) {
        setYaToken(true);
      }
    }

    getYaToken();
  }, []);

  if (ya_token) {
    return (
      <div className="App">
        <Header />
        <BlockMain create={createMusicBlock} />
        {
          blocksMusic.map((blockMusic, index) => {
            return <BlockMusic
              trackInfo={blockMusic}
              create={createMusicBlock}
              index={index + 1}
            />
          })
        }
      </div>
    );
  } else {
    return (
      <YaTokenForm />
    );
  }
}

export default App;
