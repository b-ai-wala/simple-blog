import Link from 'next/link';
import { getPostData, getAllPostSlugs } from '@/lib/posts';

export async function generateStaticParams() {
  const posts = getAllPostSlugs();
  return posts.map((post) => ({
    slug: post.slug,
  }));
}

export default async function Post({ params }: { params: { slug: string } }) {
  const postData = await getPostData(params.slug);

  return (
    <main className="container">
      <nav>
        <Link href="/">← Back to all posts</Link>
      </nav>

      <article>
        <header>
          <h1>{postData.title}</h1>
          <time>{postData.date}</time>
        </header>

        <div
          className="content"
          dangerouslySetInnerHTML={{ __html: postData.contentHtml || '' }}
        />
      </article>
    </main>
  );
}
