import React, { FC, useState } from "react";
import '../styles/App.css';
// @ts-ignore
import useSound from 'use-sound';
import { LinkCoverMusic } from "../assets/parser/LinkCoverMusic";
import api from "../api";
import supabase from "../supabase";

export const AlbumItem: FC<any> = ({ albumInfo, create, count }) => {
  const [audio, setAudio] = useState<HTMLAudioElement>();

  const addBlockMusic = () => {
    create(albumInfo);
  }

  const sizeName = (x: number): string => {
    if (x >= 100) {
      return "small";
    }
    if (x >= 50) {
      return "middle";
    }
    return "large";
  }

  const onMouseEnter = async () => {
    if (audio) {
      audio.play()
    } else {
      const response = await api.Backend.getPeakPeaksTrackIdGet(
        albumInfo.id,
        {
          headers: {
            Authorization: 'Bearer ' + (await supabase.auth.getSession()).data.session.access_token
          }
        }
      ).catch((error) => {
        console.error(error);
      });
      if (response) {
        setAudio(new Audio(response.data.download_url));
      }
    }
  }

  const onMouseLeave = async () => {
    if (audio) {
      audio.pause()
    }
  }

  return (
    <div className={`album ${sizeName(count)}`}>
      <img
        onClick={addBlockMusic}
        onMouseEnter={onMouseEnter}
        onMouseLeave={onMouseLeave}
        src={LinkCoverMusic(albumInfo.cover_url)}
        alt={albumInfo.title}
      />
    </div>
  )
}
