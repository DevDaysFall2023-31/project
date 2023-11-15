import React, { FC } from "react";
import '../styles/App.css';
import music from "../assets/music.mp3";
// @ts-ignore
import useSound from 'use-sound';
import { LinkCoverMusic } from "../assets/parser/LinkCoverMusic";

export const AlbumItem: FC<any> = ({ albumInfo, create }) => {
  const [play, { stop }] = useSound(music);
    const addBlockMusic = () => {
        create(albumInfo);
    }

  return (
    <div className="album">
      <img
        onClick={addBlockMusic}
        onMouseEnter={() => play()}
        onMouseLeave={() => stop()}
        src={LinkCoverMusic(albumInfo.cover_url)}
        alt={albumInfo.title}
      />
    </div>
  )
}