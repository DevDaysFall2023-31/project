import React, { FC, useState } from "react";
import '../styles/App.css';
import music from "../assets/music.mp3";
// @ts-ignore
import useSound from 'use-sound';
import { LinkCoverMusic } from "../assets/parser/LinkCoverMusic";

export const AlbumItem: FC<any> = ({ albumInfo, create, count }) => {
  // const [play, { stop }] = useSound(music);

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
  return (
    <div className={`album ${sizeName(count)}`}>
      <img
        onClick={addBlockMusic}
        // onMouseEnter={() => play()}
        // onMouseLeave={() => stop()}
        src={LinkCoverMusic(albumInfo.cover_url)}
        alt={albumInfo.title}
      />
    </div>
  )
}
