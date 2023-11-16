import React, { useEffect, useState, FC } from "react";

import '../styles/App.css';
import { WaveSvg } from '../assets/icons/WaveSvg';
import { AlbumSet } from "./AlbumSet";

import api from '../api';
import { GetTracksListSchema } from "../generated";
import supabase from "../supabase";

export const BlockMain: FC<any> = ({ create }) => {
  const [tracks, setTracks] = useState<GetTracksListSchema>();

  useEffect(() => {
    async function getTracks() {
      const response = await api.Backend.getFavouriteTracksTracksFavouritesGet({
        headers: {
          Authorization: 'Bearer ' + (await supabase.auth.getSession()).data.session.access_token
        }
      });
      setTracks(response.data);
    }

    getTracks();
  }, []);
  return (
    <section className="mian-block block container">
      <div className="mian-block-header">
        <h1>Что послушать.</h1>
        <WaveSvg />
      </div>
      <AlbumSet
        tracks={tracks?.tracks ?? []}
        create={create}
        count={tracks?.count ?? 0}
        glob_index={0}
      />
    </section>
  )
}
