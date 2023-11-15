import React, { FC, useState } from "react";
import '../styles/App.css';
import Like from '../assets/icons/Like.svg';
import Play from '../assets/icons/Play.svg';
import { AlbumSet } from "./AlbumSet";

export const BlockMusic: FC<any> = ({ albumInfo }) => {
  const [albums, setAlbums] = useState([
    {
      id: "1",
      img: "https://bestsellingalbums.org/covers/58126.jpg",
      title: "album"
    },
    {
      id: "2",
      img: "https://bestsellingalbums.org/covers/58126.jpg",
      title: "album"
    },
    {
      id: "3",
      img: "https://bestsellingalbums.org/covers/58126.jpg",
      title: "album"
    },
    {
      id: "4",
      img: "https://bestsellingalbums.org/covers/58126.jpg",
      title: "album"
    },
    {
      id: "5",
      img: "https://bestsellingalbums.org/covers/58126.jpg",
      title: "album"
    },
    {
      id: "6",
      img: "https://bestsellingalbums.org/covers/58126.jpg",
      title: "album"
    },
    {
      id: "7",
      img: "https://bestsellingalbums.org/covers/58126.jpg",
      title: "album"
    },
    {
      id: "8",
      img: "https://bestsellingalbums.org/covers/58126.jpg",
      title: "album"
    }
  ])
  // TODO
  return (
    <section
      className="music-block block container"
      style={{
        background: `linear-gradient(180deg, rgba(29, 33, 35, 0.80) 0%, #121212 73.96%), url(${albumInfo.img}), lightgray 50%`,
        backgroundSize: 'cover'
      }}
    >
      <div className="music-block-header">
        <img src={albumInfo.img} alt="cover" />
        <div className="music-info">
          <h2 className="music-title">{albumInfo.title}</h2>
          <p className="music-description">{albumInfo.description}</p>
          <div className="activities">
            <a href={albumInfo.ymusic}><img src={Play.toString()} alt="y.music" /><span>Я.Музыка</span></a>
            <a href="#"><img src={Like.toString()} alt="mark" /></a>
          </div>
        </div>
      </div>
      <AlbumSet tracks={[]} count={0} />
    </section>
  )
}
