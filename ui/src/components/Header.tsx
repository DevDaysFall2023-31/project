import '../styles/App.css';

export const Header = () => {
  return (
    <header className="header block container">
      <span className="logo">Слышно и точка.</span>
      <nav className="menu">
        <a href="#">Избраннное</a>
        <a href="#">Настройки</a>
        <a href="#" className="avatar">
          <img src="https://proprikol.ru/wp-content/uploads/2020/10/kartinki-nyashki-41.jpg" alt="avatar" />
        </a>
      </nav>
    </header>
  )
}
