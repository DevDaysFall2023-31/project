import React from 'react'
import supabase from '../supabase';
import '../styles/App.css';

export class YaTokenForm extends React.Component {
  state = {
    text: "",
  };

  onChange = (e: React.FormEvent<HTMLInputElement>): void => {
    this.setState({ text: e.currentTarget.value });
  };
  onSubmit = async (e: any) => {
    await supabase.auth.updateUser({
      data: {
        ya_token: this.state.text,
      }
    })
  };
  render() {
    return (
      <div className="container block container-mini">
        <div className="t-deGdmh">
          <h1>Введите ваш токен от Yandex Music</h1>
          <div className="supabase-auth-ui_ui-divider c-kbVGyA"></div>
          <form onSubmit={this.onSubmit}>
            <div className="supabase-auth-ui_ui-container c-jTXIoq c-jTXIoq-bsgKCL-direction-vertical c-jTXIoq-bXHFxK-gap-large">
              <div className="supabase-auth-ui_ui-container c-jTXIoq c-jTXIoq-bsgKCL-direction-vertical c-jTXIoq-bXHFxK-gap-large">
                <div className="">
                  <label htmlFor="y.token" className="supabase-auth-ui_ui-label c-bpexlo">Y.token</label>
                  <input
                    className="supabase-auth-ui_ui-input c-dEnagJ c-dEnagJ-bBzSYw-type-default"
                    name="y.token"
                    type="text"
                    value={this.state.text}
                    onChange={this.onChange}
                    placeholder="Y.token"
                  />
                </div>
              </div>
              <input className="supabase-auth-ui_ui-button c-bOcPnF c-bOcPnF-cmFMMs-color-primary" type="submit" value="Submit" />
              <div className="supabase-auth-ui_ui-container c-jTXIoq c-jTXIoq-bsgKCL-direction-vertical c-jTXIoq-jjTuOt-gap-small">
                <a className="supabase-auth-ui_ui-anchor c-dumjqv" href="https://yandex-music.readthedocs.io/en/main/token.html">Нет токена?</a>
              </div>
            </div>
          </form>
        </div>
      </div>
    );
  }
}
