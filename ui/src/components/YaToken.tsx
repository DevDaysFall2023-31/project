import React, { useState, useEffect } from 'react'
import { UserAttributes } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'
import { ThemeSupa } from '@supabase/auth-ui-shared'
import App from '../App';
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
      <div>
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
