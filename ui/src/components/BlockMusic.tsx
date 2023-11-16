import React, { FC, useState, useEffect } from "react";
import '../styles/App.css';
import Like from '../assets/icons/Like.svg';
import Play from '../assets/icons/Play.svg';
import { AlbumSet } from "./AlbumSet";
import { LinkCoverMusic } from '../assets/parser/LinkCoverMusic';

import api from '../api';
import { GetPeakSchema, GetTrackSchema, GetTracksListSchema } from "../generated";
import supabase from "../supabase";

export const BlockMusic: FC<{ trackInfo: GetTrackSchema, create: any, index: number }> = ({ trackInfo, create, index }) => {
  const [similar, setSimilar] = useState<GetTracksListSchema>();

  useEffect(() => {
    async function getSimilarTracks() {
      const response = await api.Backend.getSimilarTracksTracksTrackIdSimilarGet(
        trackInfo.id,
        {
          headers: {
            Authorization: 'Bearer ' + (await supabase.auth.getSession()).data.session.access_token
          }
        });
      setSimilar(response.data);
    }

    getSimilarTracks();
  }, [trackInfo.id]);

  const onLikeClick = async () => {
    await api.Backend.postLikeTrackTracksTrackIdLikePost(
      trackInfo.id,
      {
        headers: {
          Authorization: 'Bearer ' + (await supabase.auth.getSession()).data.session.access_token
        }
      }
    );
  }

  const [trackId, albumId] = trackInfo.id.split(':');
  const yaMusicLink = "https://music.yandex.ru/album/" + albumId + "/track/" + trackId;

  return (
    <section
      className="music-block block container"
      style={{
        background: `linear-gradient(180deg, rgba(29, 33, 35, 0.80) 0%, #121212 73.96%), url(${LinkCoverMusic(trackInfo.cover_url)}), lightgray 50%`,
        backgroundSize: 'cover'
      }}
    >
      <div className="music-block-header">
        <img src={LinkCoverMusic(trackInfo.cover_url)} alt="cover" />
        <div className="music-info">
          <h2 className="music-title">{trackInfo.title}</h2>
          <div className="activities">
            <a href={yaMusicLink}><img src={Play.toString()} alt="y.music" /><span>Я.Музыка</span></a>
            <button onClick={onLikeClick}><img src={Like.toString()} alt="mark" /></button>
          </div>
        </div>
      </div>
      <AlbumSet
        tracks={similar?.tracks ?? []}
        create={create}
        count={similar?.count ?? 0}
        glob_index={index}
      />
    </section >
  )
}
