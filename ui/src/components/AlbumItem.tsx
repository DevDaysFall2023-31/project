import React, { FC, useEffect, useState } from "react";
import '../styles/App.css';
import { LinkCoverMusic } from "../assets/parser/LinkCoverMusic";
import api from "../api";
import supabase from "../supabase";

export const AlbumItem: FC<any> = ({ albumInfo, peak, create, count, index }) => {
  const [audio, setAudio] = useState<HTMLAudioElement>();

  useEffect(() => {
    if (peak) {
      setAudio(new Audio(peak));
    }
  }, [peak]);

  const addBlockMusic = () => {
    create(albumInfo, index);
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
      if (response && response.data.download_url) {
        setAudio(new Audio(response.data.download_url));
        audio.play();
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
