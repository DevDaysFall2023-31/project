import { createClient } from '@supabase/supabase-js'

let supabaseKey;
let supabaseAddress;
const hostname = window && window.location && window.location.hostname;

if (hostname === 'vps.shishqa.xyz' || hostname === 'listen.shishqa.xyz') {
  supabaseAddress = 'https://emjigsoyxkedubxijerc.supabase.co';
  supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVtamlnc295eGtlZHVieGlqZXJjIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTk4ODAxNzksImV4cCI6MjAxNTQ1NjE3OX0.IT0xsTDEMLMR9BR8jNhV_n3dW5QOh-6a4A9EX58o1Og';
} else {
  supabaseAddress = 'http://localhost:54321';
  supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6ImFub24iLCJleHAiOjE5ODM4MTI5OTZ9.CRXP1A7WOeoJeXxjNni43kdQwgnWNReilDMblYTn_I0';
}

const supabase = createClient(supabaseAddress, supabaseKey);

export default supabase;
