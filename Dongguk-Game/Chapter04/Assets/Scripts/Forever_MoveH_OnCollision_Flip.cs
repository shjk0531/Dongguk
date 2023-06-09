using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// 계속 이동하고, 충돌하면 반전한다(수평)
public class Forever_MoveH_OnCollision_Flip : MonoBehaviour
{

    public float speed = 1; // 속도: Inspector에 지정

    Rigidbody2D rbody;

    // Start is called before the first frame update
    void Start()    // 처음에 시행한다
    {
        // 중력을 0으로 해서 충돌 시에 회전시키지 않는다
        rbody = GetComponent<Rigidbody2D>();
        rbody.gravityScale = 0;
        rbody.constraints = RigidbodyConstraints2D.FreezeRotation;
    }

    private void FixedUpdate()  // 계속 시행한다(일정 시간마다)
    {
        // 수평으로 이동한다
        rbody.velocity = new Vector2(speed, 0);
    }

    private void OnCollisionEnter2D(Collision2D collision)  // 충돌했을 때
    {
        speed = -speed; // 나아가는 방향을 반전시킨다
                        // 나아가는 방향에서 왼쪽 오른쪽의 방향을 바꾼다
        this.GetComponent<SpriteRenderer>().flipX = (speed < 0);
    }

}
