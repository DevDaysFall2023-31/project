INSERT INTO storage.buckets
    (id, name)
VALUES
    ('y_storage', 'y_storage');

CREATE POLICY "Public Access"
    ON storage.objects for SELECT
    USING ( bucket_id = 'public' );

CREATE POLICY "full_access_i"
    ON storage.objects FOR INSERT TO anon
    WITH CHECK (bucket_id = 'y_storage');

CREATE POLICY "full_access_s"
    ON storage.objects FOR SELECT TO anon
    USING (bucket_id = 'y_storage');
