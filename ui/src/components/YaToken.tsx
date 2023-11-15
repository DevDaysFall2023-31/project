import React from 'react'
import supabase from '../supabase';

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
        <h1>Введите ваш токен от Yandex Music:</h1>
        <form onSubmit={this.onSubmit}>
          <input
            type="text"
            value={this.state.text}
            onChange={this.onChange}
          />
          <input type="submit" value="Submit" />
        </form>
      </div>
    );
  }
}
