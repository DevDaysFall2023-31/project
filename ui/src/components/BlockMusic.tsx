import React, { FC, useState, useEffect } from "react";
import '../styles/App.css';
import Like from '../assets/icons/Like.svg';
import Play from '../assets/icons/Play.svg';
import { AlbumSet } from "./AlbumSet";
import { LinkCoverMusic } from '../assets/parser/LinkCoverMusic';

import api from '../api';
import { GetPeakSchema } from "../generated";

export const BlockMusic: FC<any> = ({ albumInfo, create }) => {
  const [tracks, setTracks] = useState<GetPeakSchema>();

  useEffect(() => {
    async function getTracks() {
      const response = await api.Backend.getPeakPeaksTrackIdGet(albumInfo.id);
      setTracks(response.data);
    }

    getTracks();
  }, []);
  console.log(tracks, albumInfo.id);
  // TODO
  return (
    <section
      className="music-block block container"
      style={{
        background: `linear-gradient(180deg, rgba(29, 33, 35, 0.80) 0%, #121212 73.96%), url(${LinkCoverMusic(albumInfo.cover_url)}), lightgray 50%`,
        backgroundSize: 'cover'
      }}
    >
      <div className="music-block-header">
        <img src={LinkCoverMusic(albumInfo.cover_url)} alt="cover" />
        <div className="music-info">
          <h2 className="music-title">{albumInfo.title}</h2>
          <p className="music-description">{albumInfo.description}</p>
          <div className="activities">
            <a href={albumInfo.ymusic}><img src={Play.toString()} alt="y.music" /><span>Я.Музыка</span></a>
            <a href="#"><img src={Like.toString()} alt="mark" /></a>
          </div>
        </div>
      </div>
      <AlbumSet tracks={[]} create={create} /* count={0} */ />
    </section>
  )
}