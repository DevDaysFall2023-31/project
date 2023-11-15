import React, { useEffect, useState } from "react";

import '../styles/App.css';
import { WaveSvg } from '../assets/icons/WaveSvg';
import { AlbumSet } from "./AlbumSet";

import api from '../api';
import { GetTracksListSchema } from "../generated";

export const BlockMain = () => {
  const [tracks, setTracks] = useState<GetTracksListSchema>();

  useEffect(() => {
    async function getTracks() {
      const response = await api.Backend.getFavouriteTracksTracksFavouritesGet();
      setTracks(response.data);
    }

    getTracks();
  }, []);

  return (
    <section className="mian-block block container">
      <div className="mian-block-header">
        <h1>Что послушать.</h1>
        <p>У вас {tracks?.count} треков</p>
        <WaveSvg />
      </div>
      <AlbumSet
        tracks={tracks?.tracks ?? []}
        count={tracks?.count ?? 0}
      />
    </section>
  )
}
